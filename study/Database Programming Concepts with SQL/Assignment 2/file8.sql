SELECT * FROM Clients 
WHERE ClientID IN (SELECT ClientID FROM Transactions WHERE TransactionType = 'Purchase');

SELECT ListingAgentID, COUNT(*) AS PropertyCount 
FROM Properties 
GROUP BY ListingAgentID;

SELECT SellingAgentID, SUM(CommissionAmount) AS TotalCommission 
FROM Transactions 
GROUP BY SellingAgentID;
