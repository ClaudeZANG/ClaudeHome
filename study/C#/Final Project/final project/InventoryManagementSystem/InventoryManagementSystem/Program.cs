using System;

namespace InventoryManagementSystem
{
    class Program
    {
        static void Main(string[] args)
        {
            InventoryManager manager = new InventoryManager();
            bool exit = false;
            while (!exit)
            {
                Console.WriteLine("Inventory Management System");
                Console.WriteLine("1. Add New Item");
                Console.WriteLine("2. Display Specific Item");
                Console.WriteLine("3. Display All Items");
                Console.WriteLine("4. Exit");
                Console.WriteLine("5. Display All Item IDs");
                Console.WriteLine("6. Display Item With Highest Price");
                Console.WriteLine("7. Sort Items By Price");
                Console.Write("Please select an option: ");
                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        manager.AddNewItem();
                        break;
                    case "2":
                        manager.DisplaySpecificItem();
                        break;
                    case "3":
                        manager.DisplayAllItems();
                        break;
                    case "4":
                        exit = true;
                        break;
                    case "5":
                        manager.DisplayAllItemIDs();
                        break;
                    case "6":
                        manager.DisplayItemWithHighestPrice();
                        break;
                    case "7":
                        manager.SortItemsByPrice();
                        break;
                    default:
                        Console.WriteLine("Invalid option. Please select a valid option.");
                        break;
                }
            }
        }
    }
}
