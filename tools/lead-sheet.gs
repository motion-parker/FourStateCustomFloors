// Four State Custom Floors – website lead catcher (temporary, until the GHL sub-account is ready)
//
// Paste this whole file into the Google Sheet: Extensions → Apps Script.
// Every estimate request from the website becomes a row in the sheet,
// photos are saved to a Drive folder, and an email alert goes out.

const ALERT_EMAILS = "PUT-EMAIL-HERE";            // who gets new-lead emails; separate several with commas
const PHOTO_FOLDER = "Website lead photos";       // Drive folder for uploaded photos (created automatically)

const HEADERS = ["Received", "Name", "Phone", "Town", "Project", "Timing", "Message",
                 "Photos", "Ad source", "Ad medium", "Ad campaign", "Page"];

function doPost(e) {
  try {
    const d = JSON.parse(e.postData.contents);

    // Spam trap: real people never see or fill the "website" field
    if (d.website) return reply({ ok: true });
    if (!d.name || !d.phone) return reply({ ok: false, error: "Name and phone are required" });

    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(HEADERS);
      sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight("bold");
      sheet.setFrozenRows(1);
    }

    const links = savePhotos(d.photos || [], d.name);
    const row = [new Date(), clean(d.name), clean(d.phone), clean(d.town), clean(d.project),
                 clean(d.timing), clean(d.message), links.join("\n"),
                 clean(d.utm_source), clean(d.utm_medium), clean(d.utm_campaign), clean(d.page)];
    sheet.appendRow(row);

    sendAlert(d, links);
    return reply({ ok: true });
  } catch (err) {
    return reply({ ok: false, error: String(err) });
  }
}

function savePhotos(photos, name) {
  if (!photos.length) return [];
  const it = DriveApp.getFoldersByName(PHOTO_FOLDER);
  const folder = it.hasNext() ? it.next() : DriveApp.createFolder(PHOTO_FOLDER);
  const stamp = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd HHmm");
  return photos.slice(0, 5).map(function (p, i) {
    const blob = Utilities.newBlob(Utilities.base64Decode(p.data), "image/jpeg",
                                   stamp + " " + clean(name) + " " + (i + 1) + ".jpg");
    return folder.createFile(blob).getUrl();
  });
}

function sendAlert(d, links) {
  if (!ALERT_EMAILS || ALERT_EMAILS.indexOf("@") === -1) return;
  const phone = clean(d.phone), digits = phone.replace(/[^0-9+]/g, "");
  const lines = [
    "New estimate request from the website",
    "",
    "Name: " + clean(d.name),
    "Phone: " + phone,
    "Town: " + (clean(d.town) || "-"),
    "Project: " + (clean(d.project) || "-"),
    "Timing: " + (clean(d.timing) || "-"),
    "Message: " + (clean(d.message) || "-"),
    "Photos: " + (links.length ? "\n" + links.join("\n") : "none"),
    "",
    "Call: tel:" + digits,
    "Text: sms:" + digits,
    "",
    "All leads: " + SpreadsheetApp.getActiveSpreadsheet().getUrl()
  ];
  MailApp.sendEmail(ALERT_EMAILS, "New lead: " + clean(d.name) + " – " + (clean(d.project) || "website"), lines.join("\n"));
}

function clean(v) {
  // Stops anything typed into the form from being read as a spreadsheet formula
  const s = String(v == null ? "" : v).trim().slice(0, 3000);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}

function reply(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

// Run this once from the editor (select "setup", click Run) to grant permissions before deploying.
function setup() {
  const it = DriveApp.getFoldersByName(PHOTO_FOLDER);
  if (!it.hasNext()) DriveApp.createFolder(PHOTO_FOLDER);
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(HEADERS);
    sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight("bold");
    sheet.setFrozenRows(1);
  }
  if (ALERT_EMAILS.indexOf("@") !== -1) MailApp.getRemainingDailyQuota();
}
