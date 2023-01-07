<pre class='mermaid'>
classDiagram
    direction LR

    %% Class Relationships
    BluePrint --|> AbstractBaseClass
    GreenField --|> BluePrint
    RedField --|> BluePrint

    %% Class Attributes
    class AbstractBaseClass {
        << abstract>>
    }

    class BluePrint {
       << abstract>>
       hello()*
    }

    class GreenField {
        hello()
    }

    class RedField {
        hello()
    }
</pre>

<pre class='mermaid'>
classDiagram
    direction BT
    
    %% Class Relationships
    MFD1 --|> Scanner
    MFD1 --|> Printer
    
    


    MFD2 --|> Scanner
    MFD2 --|> Printer
    
    

    MFD3 --|> Scanner
    MFD3 --|> Printer
    
    MFD3 "1" o-- "*" PrintJob
    MFD2 "1" o-- "*" PrintJob

    %% Class Definitions
    class Scanner {
        << abstract>>
        scan_document()* String
        get_scanner_status()* ScannerInfo 
    }

    class PrintJob {
        document: str
        time: DateTime
    }

    class Printer {
        << abstract>>
        print_document()* String()
        get_printer_status()* PrinterInfo
    }

    class MFD1 {
        scanner_info: ScannerInfo
        printer_info: PrinterInfo
        scan_document(): String
        print_document(): String
        get_scanner_status(): ScannerInfo
        get_printer_status(): PrinterInfo
        _get_next_serial_number()$ String
        _increment_serial()$
    }

    class MFD2 {
        scanner_info: ScannerInfo
        printer_info: PrinterInfo
        print_history: List~PrintJob~
        scan_document(): String
        print_document(): String
        get_scanner_status(): ScannerInfo
        get_printer_status(): PrinterInfo
        printing_operation_history() List~PrintJob~
        _get_next_serial_number()$ String
        _increment_serial()$
    }

        class MFD3 {
        scanner_info: ScannerInfo
        printer_info: PrinterInfo
        print_history: List~PrintJob~
        scan_document(): String
        print_document(): String
        fax_document(): String
        get_scanner_status(): ScannerInfo
        get_printer_status(): PrinterInfo
        printing_operation_history() List~PrintJob~
        _get_next_serial_number()$ String
        _increment_serial()$

    }



</pre>

<pre class='mermaid'>
classDiagram
    MFD1 "*" o-- "1" ScannerInfo
    MFD1 "*" o-- "1" PrinterInfo
    MFD2 "*" o-- "1" ScannerInfo
    MFD2 "*" o-- "1" PrinterInfo
    MFD3 "*" o-- "1" ScannerInfo
    MFD3 "*" o-- "1" PrinterInfo

    class ScannerInfo {
        String max_resolution
        String serial_number
        to_string() String
    }

    class PrinterInfo {
        String max_resolution
        String serial_number
        to_string() String
    }
</pre>
