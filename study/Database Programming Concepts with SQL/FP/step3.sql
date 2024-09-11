CREATE TABLE Employees (
    EmployeeID VARCHAR(10) PRIMARY KEY,        -- Employee number, set as primary key
    LoginID VARCHAR(50),                      -- Login ID
    Password VARCHAR(50),                     -- password
    GroupType VARCHAR(50),                    -- Group
    FirstName VARCHAR(50),                    -- First name
    LastName VARCHAR(50),                     -- Last name
    SocialInsuranceNumber VARCHAR(15) UNIQUE, -- SIN, set to be unique
    PhoneOffice VARCHAR(10)                   -- phone NO.
);
