using System;

namespace ItemPriceManagement
{
    public class Item
    {
        public string Iname { get; set; }
        public int Id { get; set; }
        public string SerialNumber { get; set; }

        public Item(string iname, int id, string serialNumber)
        {
            Iname = iname;
            Id = id;
            SerialNumber = serialNumber;
        }
    }

    public class Price
    {
        public int Id { get; set; }
        public decimal ItemPrice { get; set; }

        public Price(int id, decimal itemPrice)
        {
            Id = id;
            ItemPrice = itemPrice;
        }
    }
}
