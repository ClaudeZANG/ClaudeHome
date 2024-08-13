function initMap() {
    // The location of Uluru
    const position = { lat: -25.344, lng: 131.031 };

    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: position,
        mapId: "DEMO_MAP_ID", // 请替换为您的Map ID
    });

    // The advanced marker, positioned at Uluru
    const marker = new google.maps.marker.AdvancedMarkerElement({
        position: position,
        map: map,
        title: 'Uluru',
    });
}

// 确保initMap函数在全局作用域内，以便在API加载完成时调用
window.initMap = initMap;
