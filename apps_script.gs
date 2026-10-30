/**
 * Paste into your Google Sheet: Extensions > Apps Script > replace everything > Save.
 * First time: click Run once on onEdit is NOT needed; just save. It stamps the REAL time automatically:
 *  - when you type Yes in "Done? (type Yes)" on Today Queue  -> fills "Sent At (auto)"
 *  - when you type Yes in "Replied? (Yes/No)" on Outreach Log -> fills "Replied At (auto)"
 */
function onEdit(e) {
  if (!e || !e.range) return;
  var sh = e.range.getSheet(), name = sh.getName();
  var hdr = sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0];
  function stamp(watch, target) {
    var w = hdr.indexOf(watch) + 1, s = hdr.indexOf(target) + 1;
    if (!w || !s || e.range.getColumn() > w || e.range.getLastColumn() < w) return;
    var now = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd HH:mm");
    for (var r = Math.max(2, e.range.getRow()); r <= e.range.getLastRow(); r++) {
      var v = String(sh.getRange(r, w).getValue()).trim().toLowerCase();
      sh.getRange(r, s).setValue(v === "yes" ? now : "");
    }
  }
  if (name === "Today Queue") stamp("Done? (type Yes)", "Sent At (auto)");
  if (name === "Outreach Log") stamp("Replied? (Yes/No)", "Replied At (auto)");
}
