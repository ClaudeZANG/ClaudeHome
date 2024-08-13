namespace MvcMusicStore.Models
{
    public class Order
    {
        public int Id { get; set; }
        public string UserId { get; set; }
        public DateTime OrderDate { get; set; }
        public string ShippingAddress { get; set; }
        public string ContactNumber { get; set; }
        public decimal TotalAmount { get; set; }
    }
}
