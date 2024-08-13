using System;
using System.Linq;
using System.Collections.Generic;

namespace InventoryManagementSystem
{
    internal class InventoryManager
    {
        // List to store items
        private List<Item> items = new List<Item>();

        // Method to add a new item
        public void AddNewItem()
        {
            bool addMore = true;
            while (addMore)
            {
                string id = GenerateNextID();
                Console.WriteLine($"Auto-generated ID: {id}");

                Console.Write("Please enter the item's first name: ");
                string firstName = Console.ReadLine();
                Console.Write("Please enter the item's description: ");
                string lastName = Console.ReadLine();
                Console.Write("Please enter the price: ");
                double price;
                while (!double.TryParse(Console.ReadLine(), out price))
                {
                    Console.Write("Invalid input, please enter a valid price: ");
                }

                // Create a new item and add it to the list
                Item newItem = new Item { ID = id, FirstName = firstName, LastName = lastName, Price = price };
                items.Add(newItem);

                Console.Write("Do you want to add another item? (y/n): ");
                addMore = Console.ReadLine().ToLower() == "y";
            }
        }

        public void DisplayAllItemIDs()
        {
            Console.WriteLine("All available item IDs:");
            foreach (var item in items)
            {
                Console.WriteLine($"ID: {item.ID}");
            }
            Console.WriteLine("Press any key to return to menu.");
            Console.ReadKey();
        }

        public void DisplayItemWithHighestPrice()
        {
            var itemWithHighestPrice = items.OrderByDescending(i => i.Price).FirstOrDefault();
            if (itemWithHighestPrice != null)
            {
                Console.WriteLine("Item with highest price:");
                Console.WriteLine($"ID: {itemWithHighestPrice.ID}");
                Console.WriteLine($"First Name: {itemWithHighestPrice.FirstName}");
                Console.WriteLine($"Last Name: {itemWithHighestPrice.LastName}");
                Console.WriteLine($"Price: ${itemWithHighestPrice.Price}");
            }
            else
            {
                Console.WriteLine("No items found.");
            }
            Console.WriteLine("Press any key to return to menu.");
            Console.ReadKey();
        }

        private string GenerateNextID()
        {
            // Generate the next sequential ID
            if (items.Count == 0)
            {
                return "001";
            }
            else
            {
                int lastID = int.Parse(items.Last().ID);
                int nextID = lastID + 1;
                return nextID.ToString().PadLeft(3, '0');
            }
        }

        public void DisplaySpecificItem()
        {
            Console.Write("Please enter the item ID to display: ");
            string id = Console.ReadLine();
            var item = items.FirstOrDefault(i => i.ID == id);
            if (item != null)
            {
                Console.WriteLine($"ID: {item.ID}");
                Console.WriteLine($"First Name: {item.FirstName}");
                Console.WriteLine($"Last Name: {item.LastName}");
                Console.WriteLine($"Price: ${item.Price}");
            }
            else
            {
                Console.WriteLine("Item not found.");
            }
            Console.WriteLine("Press any key to return to menu.");
            Console.ReadKey();
        }

        public void DisplayAllItems()
        {
            Console.WriteLine("All items in inventory:");
            foreach (var item in items)
            {
                Console.WriteLine($"ID: {item.ID}, First Name: {item.FirstName}, Last Name: {item.LastName}, Price: ${item.Price}");
            }
            Console.WriteLine("Press any key to return to menu.");
            Console.ReadKey();
        }

        public void SortItemsByPrice()
        {
            var sortedItems = items.OrderBy(i => i.Price).ToList();
            Console.WriteLine("Items sorted by price:");
            foreach (var item in sortedItems)
            {
                Console.WriteLine($"ID: {item.ID}, First Name: {item.FirstName}, Last Name: {item.LastName}, Price: ${item.Price}");
            }
            Console.WriteLine("Press any key to return to menu.");
            Console.ReadKey();
        }
    }

    // Define the Item class
    internal class Item
    {
        public string ID { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public double Price { get; set; }
    }
}
