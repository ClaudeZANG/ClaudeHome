CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Address VARCHAR(255),
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100),
    Position VARCHAR(50),
    EmployeeType VARCHAR(20),
    RealEstateLicenseNumber VARCHAR(20),
    CommissionRate DECIMAL(5, 2),
    HireDate DATE,
    Salary DECIMAL(10, 2)
);

-- 创建 Clients 表
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100),
    PreferredContactMethod VARCHAR(20),
    AgentID INT,
    SearchCriteria VARCHAR(255),
    FOREIGN KEY (AgentID) REFERENCES Employees(EmployeeID)
);

-- 插入数据到 Employees 表
INSERT INTO Employees (EmployeeID, FirstName, LastName, Address, PhoneNumber, Email, Position, EmployeeType, RealEstateLicenseNumber, CommissionRate, HireDate, Salary) VALUES
(1, 'John', 'Doe', '123 Elm St', '123-456-7890', 'john.doe@example.com', 'Agent', 'Full-time', 'A12345', 3.00, '2023-01-01', 60000.00),
(2, 'Jane', 'Smith', '456 Oak St', '987-654-3210', 'jane.smith@example.com', 'Agent', 'Full-time', 'B67890', 3.00, '2023-01-01', 65000.00),
(3, 'Emily', 'Johnson', '789 Pine St', '555-555-5555', 'emily.johnson@example.com', 'Agent', 'Independent', 'C54321', 5.00, '2023-01-01', NULL),
(4, 'Michael', 'Brown', '101 Maple St', '444-444-4444', 'michael.brown@example.com', 'Admin', 'Full-time', NULL, NULL, '2023-01-01', 40000.00),
(5, 'Sarah', 'Davis', '202 Birch St', '333-333-3333', 'sarah.davis@example.com', 'HR', 'Full-time', NULL, NULL, '2023-01-01', 50000.00);

-- 插入数据到 Clients 表
INSERT INTO Clients (ClientID, FirstName, LastName, PhoneNumber, Email, PreferredContactMethod, AgentID, SearchCriteria) VALUES
(1, 'Alice', 'Brown', '111-111-1111', 'alice.brown@example.com', 'Email', 1, 'Detached, $300000-$400000, 3 bedrooms'),
(2, 'Bob', 'Green', '222-222-2222', 'bob.green@example.com', 'Phone', 2, 'Condo, $200000-$300000, 2 bedrooms');

CREATE TABLE Properties (
    PropertyID INT PRIMARY KEY,
    ListingNumber VARCHAR(20) UNIQUE,
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(50),
    ZipCode VARCHAR(10),
    Price DECIMAL(15, 2),
    PropertyType VARCHAR(50),
    Bedrooms INT,
    Bathrooms INT,
    SquareFootage INT,
    ListingAgentID INT,
    FOREIGN KEY (ListingAgentID) REFERENCES Employees(EmployeeID)
);


CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY,
    TransactionType VARCHAR(20),
    TransactionDate DATE,
    TransactionAmount DECIMAL(15, 2),
    ClientID INT,
    PropertyID INT,
    SellingAgentID INT,
    CommissionAmount DECIMAL(10, 2),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID),
    FOREIGN KEY (SellingAgentID) REFERENCES Employees(EmployeeID)
);

INSERT INTO Properties (PropertyID, ListingNumber, Address, City, State, ZipCode, Price, PropertyType, Bedrooms, Bathrooms, SquareFootage, ListingAgentID) VALUES
(1, 'LN001', '123 Elm St', 'New York', 'NY', '10001', 350000.00, 'Detached', 3, 2, 1500, 1),
(2, 'LN002', '456 Oak St', 'Los Angeles', 'CA', '90001', 250000.00, 'Condo', 2, 1, 1000, 2);

INSERT INTO Transactions (TransactionID, TransactionType, TransactionDate, TransactionAmount, ClientID, PropertyID, SellingAgentID, CommissionAmount) VALUES
(1, 'Purchase', '2024-08-01', 350000.00, 1, 1, 1, 10500.00),
(2, 'Rental', '2024-08-02', 2000.00, 2, 2, 2, 60.00);


