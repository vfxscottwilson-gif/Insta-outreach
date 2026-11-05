# Saves the Supabase secret key that is on the clipboard into the private secrets file. Never prints the key or any part of the clipboard.
# Usage: copy the key in the Supabase dashboard (API Keys > Secret keys > default > copy), then run this script.
$k = (Get-Clipboard -Raw)
if ($null -eq $k) { Write-Output 'Clipboard is empty. Copy the secret key first.'; exit 1 }
$k = $k.Trim()
if ($k -notmatch '^sb_secret_\S{20,}$') { Write-Output ('Clipboard does not hold a Supabase secret key (length ' + $k.Length + '). Nothing saved.'); exit 1 }
$f = Join-Path (Split-Path $PSScriptRoot -Parent) 'secrets\supabase-backup.env'
Set-Content -Path $f -Encoding ascii -Value @('SUPABASE_URL=https://ogtipywmtoiaaqvllhjg.supabase.co', 'SUPABASE_BUCKET=database-backups', ('SUPABASE_SECRET_KEY=' + $k))
Set-Clipboard -Value ' '
Write-Output ('Saved the key to secrets\supabase-backup.env (length ' + $k.Length + ', value not shown) and cleared the clipboard.')
