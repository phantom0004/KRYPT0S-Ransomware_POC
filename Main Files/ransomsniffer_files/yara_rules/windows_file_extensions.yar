rule windows_executable_extension_rule
{
    meta:
        author = "Daryl Gatt"
        description = "Checks if the file is a compiled windows executable."
        date = "2024-09-12"

    strings:
        // Hexadecimal Values
        $exe = {4D 5A}  // .exe files
        $com = {4D 5A}  // .com files
        $bat = "echo"   // Simple batch file (BAT)
        $scr = {4D 5A}  // Screensaver files (.scr)
        $msi = {D0 CF 11 E0 A1 B1 1A E1}  // .msi Windows Installer files use the OLE Compound Format
        $wsf = {3C 3F 78 6D 6C} // .wsf files
    
    condition:
        any of them at 0
}

rule windows_script_rule
{
    meta:
        author = "Daryl Gatt"
        description = "Detects windows related scripts."
        date = "2024-09-13"

    strings:
        // .bat & .cmd files (Batch Files)
        $bat_print  = "echo" nocase
        $bat_file_start = "@echo off" nocase
        $bat_comment = "rem" nocase

        // .vba files (Visual Basic for Applications)
        $vba_variable_define = "Dim" nocase
        $vba_string_start = "Sub" nocase
        $vba_string_end = "End Sub" nocase

        // .ps1 files (Powershell)
        $powershell_paramater = "param(" nocase
        $powershell_print = "Write_Host" nocase

        // .wsf files (Windows Script File)
        $wsf_root_element = "<job>" nocase
        $wsf_message_box = "MsgBox" nocase
        $wsf_console_output = "WScript.Echo" nocase

        // .vbs files (Virtual Basic File)
        $vbs_script_tag = "<script language=\"VBScript\"" nocase
        $vbs_create_object = "CreateObject" nocase
        
    condition:
        any of them 
}

rule office_extension_rule
{
    meta:
        author = "Daryl Gatt"
        description = "Checks if the file is a Microsoft Office document."
        date = "2024-09-12"

    strings:
        // Legacy Microsoft Office formats (Word, Excel, PowerPoint, Publisher, Visio) (ZIP Documents = Modern Word Documents)
        $office_legacy = {D0 CF 11 E0 A1 B1 1A E1}  // OLE Compound File Format for .doc, .xls, .ppt, .pub, .vsd

        // Modern Office formats (Word, Excel, PowerPoint, macro-enabled)
        $word_docx = {50 4B 03 04}  // ZIP format for .docx
        $word_docm = {50 4B 03 04}  // ZIP format for .docm (macro-enabled Word files)
        $excel_xlsx = {50 4B 03 04}  // ZIP format for .xlsx
        $excel_xlsm = {50 4B 03 04}  // ZIP format for .xlsm (macro-enabled Excel files)
        $pptx = {50 4B 03 04}  // ZIP format for .pptx
        $pptm = {50 4B 03 04}  // ZIP format for .pptm (macro-enabled PowerPoint files)

        // PDF file
        $pdf = {25 50 44 46 2D}  // "%PDF-" magic number for PDF files

        // RTF file
        $rtf = {7B 5C 72 74 66 31}  // "rtf1" magic number for RTF files

        // OpenDocument formats (LibreOffice and OpenOffice)
        $odt = {50 4B 03 04}  // ZIP format for .odt
        $ods = {50 4B 03 04}  // ZIP format for .ods
        $odp = {50 4B 03 04}  // ZIP format for .odp

        // Microsoft OneNote files
        $onenote = {E4 52 5C 7B 8C D8 A4 1D}  // Magic number for OneNote .one files

        // Excel binary format
        $excel_xlsb = {D0 CF 11 E0 A1 B1 1A E1}  // Excel binary format (legacy .xlsb)

    condition:
        any of them at 0
}

