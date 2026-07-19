graph TD
    %% -------------------------------------------------------------------------
    %% Class/IS-A Structure (Taxonomy)
    %% -------------------------------------------------------------------------
    
    subgraph CoreTaxonomy [Entity Classification]
        subgraph MaterialTypes [Material Concept]
            LibraryMaterial(<b>LibraryMaterial</b><br/><i>Core Concept</i>)
        end
        
        subgraph SubMaterialTypes [Subclasses]
            PhysicalCopy(<b>PhysicalCopy</b>)
            DigitalResource(<b>DigitalResource</b>)
            Periodical(<b>Periodical</b>)
        end
    end
    
    subgraph HumanClassification [Actors]
        LibraryActor(<b>LibraryActor</b>)
        
        %% Patron Sub-subclasses
        subgraph PatronTypes [Types of Patrons]
            LibraryPatron(<b>LibraryPatron</b>)
            MemberPatron(MemberPatron)
            StaffPatron(StaffPatron)
        end
        
        subgraph EmployeeTypes [Staff Types]
            LibraryEmployee(<b>LibraryEmployee</b>)
            Librarian(Librarian)
            Admin(SystemAdmin)
        end
    end

    %% Hierarchy edges
    DigitalResource --IS-A--> LibraryMaterial
    PhysicalCopy --IS-A--> LibraryMaterial
    Periodical --IS-A--> LibraryMaterial
    
    LibraryPatron --IS-A--> LibraryActor
    LibraryEmployee --IS-A--> LibraryActor
    MemberPatron --IS-A--> LibraryPatron
    StaffPatron --IS-A--> LibraryPatron
    Librarian --IS-A--> LibraryEmployee
    Admin --IS-A--> LibraryEmployee

    %% -------------------------------------------------------------------------
    %% The Bibliographic Database (The Abstract Records)
    %% -------------------------------------------------------------------------
    
    subgraph BibliographicRecord [Abstract Database Entry]
        BookMetadata(<b>BookMetadata</b><br/><i>Title Record</i>)
    end
    
    subgraph AttributeNodes [Metadata Attributes]
        ISBNValue(<u>ISBN: 978-0...</u>)
        BookTitleVal(<u>Title: 'The...'</u>)
        PubDateVal(<u>Published: 19XX</u>)
        SubjectVal(<u>Subject: Fiction</u>)
    end
    
    subgraph SpecificEntityNodes [Creator Nodes]
        AuthorNode(Author:<br/>Orwell)
        PublisherNode(Publisher:<br/>Penguin)
    end
    
    BookMetadata --HAS_TITLE--> BookTitleVal
    BookMetadata --HAS_UNIQUE_ID--> ISBNValue
    BookMetadata --WRITTEN_BY--> AuthorNode
    BookMetadata --PUBLISHED_BY--> PublisherNode
    BookMetadata --RELEASED_DATE--> PubDateVal
    BookMetadata --HAS_SUBJECT--> SubjectVal

    %% -------------------------------------------------------------------------
    %% Linking Record to Object (The Library Inventory)
    %% -------------------------------------------------------------------------
    
    subgraph Inventory [The Physical Copies]
        BookCopy_1(Copy: #XYZ-A)
        BookCopy_2(Copy: #XYZ-B)
    end
    
    subgraph LocationStatusNodes [Location and State]
        ShelvingArea(<b>ShelvingArea</b>)
        Shelf_3B(Shelf location:<br/>'Aisle 3, Row B')
        STATUS_Available(STATE:<br/>Available)
        STATUS_Reserved(STATE:<br/>Reserved)
    end
    
    %% Essential Connection
    BookCopy_1 --IS_INSTANCE_OF--> BookMetadata
    BookCopy_2 --IS_INSTANCE_OF--> BookMetadata
    
    BookCopy_1 --IS_CURRENTLY_AT--> Shelf_3B
    BookCopy_2 --HAS_STATUS--> STATUS_Reserved
    BookCopy_1 --HAS_STATUS--> STATUS_Available
    ShelvingArea --CONTAINS--> Shelf_3B

    %% -------------------------------------------------------------------------
    %% Actors and Account Constraints
    %% -------------------------------------------------------------------------
    
    subgraph ActiveAccounts [The Users]
        Patron_123(Patron: #123A)
        Librarian_Mary(Librarian:<br/>Mary)
    end
    
    subgraph AccountLimits [Rules]
        BorrowLimit_5(LIMIT:<br/>Borrow max 5)
        MaxDays_21(LIMIT:<br/>21 Day max)
    end

    Patron_123 --IS_INSTANCE_OF--> MemberPatron
    Patron_123 --HAS_CONSTRAINT--> BorrowLimit_5
    BorrowLimit_5 --SPECIFIES--> MaxDays_21
    Librarian_Mary --IS_INSTANCE_OF--> Librarian
    
    %% Constraint relationship (Admin sets limits)
    Admin --DEFINES--> AccountLimits

    %% -------------------------------------------------------------------------
    %% The Transactions (The Temporary States)
    %% -------------------------------------------------------------------------
    
    subgraph Transactions [Active Loan/Reservation Events]
        CurrentLoan(ActiveLoan:<br/>Loan#1001)
        CurrentReservation(Reservation:<br/>Res#202)
    end
    
    %% The dashed edges indicate dynamic links
    %% Process edges
    Patron_123 -. initiates .-> CurrentLoan
    CurrentLoan -. BORROWS .-x BookCopy_1
    
    Librarian_Mary -. manages/approves .-> CurrentLoan
    
    Patron_123 -. creates .-> CurrentReservation
    CurrentReservation -. RESERVES .-> BookMetadata
    
    BookMetadata -. can_notify_of_availability .-> Patron_123