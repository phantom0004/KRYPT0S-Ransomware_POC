rule windows_exe_extension_checker
{
    meta:
        author = "Daryl Gatt"
        description = "Checks if the file is a compiled windows executable."
        date = "2024-09-12"

    strings:
        // Windows Compiled Executable File
        $exe_magic_hex_value = {4D 5A} // Format for .exe files
    
    condition:
        $exe_magic_hex_value at 0
}

rule office_extension_checker
{
    meta:
        author = "Daryl Gatt"
        description = "Checks if the file is a Microsoft office document."
        date = "2024-09-12"

    strings:
        // Legacy Microsoft Office formats (Word, Excel, PowerPoint, Publisher, Visio)
        $office_legacy = {D0 CF 11 E0 A1 B1 1A E1}  // OLE Compound File Format for .doc, .xls, .ppt, .pub, .vsd

        // Modern Office formats (Word, Excel, PowerPoint)
        $word_docx = {50 4B 03 04}  // ZIP format for .docx
        $excel_xlsx = {50 4B 03 04}  // ZIP format for .xlsx
        $pptx = {50 4B 03 04}  // ZIP format for .pptx

        // PDF file
        $pdf = {25 50 44 46 2D}  // "%PDF-" magic number for PDF files

        // RTF file
        $rtf = {7B 5C 72 74 66 31}  // "rtf1" magic number for RTF files

        // OpenDocument formats (LibreOffice and OpenOffice)
        $odt = {50 4B 03 04}  // ZIP format for .odt
        $ods = {50 4B 03 04}  // ZIP format for .ods
        $odp = {50 4B 03 04}  // ZIP format for .odp
    
    condition:
        any of them at 0
}

rule image_extension_checker
{
    meta:
        author = "Daryl Gatt"
        description = "Checks if the file is in an image format."
        date = "2024-09-12"

    strings:
        $jpg = {FF D8 FF}  // JPEG files
        $png = {89 50 4E 47 0D 0A 1A 0A}  // PNG files
        $gif = {47 49 46 38}  // GIF files
        $bmp = {42 4D}  // BMP files
        $tiff_be = {4D 4D 00 2A}  // TIFF (Big Endian)
        $tiff_le = {49 49 2A 00}  // TIFF (Little Endian)
        $webp = {52 49 46 46}  // WebP files start with "RIFF"
        $ico = {00 00 01 00}  // ICO files (Windows icon format)

    condition:
        any of them at 0 
}

rule 