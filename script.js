document.getElementById("search-button").addEventListener("click", function () {
    const artistName = document.getElementById("search-input").value;
    if (artistName) {
        fetchArtistInfo(artistName);
    }
});

function fetchArtistInfo(artistName) {
    const loading = document.getElementById("loading");
    const artistInfo = document.getElementById("artist-info");


    loading.classList.remove("hidden");
    artistInfo.classList.add("hidden");


    fetch(`/api/artist/${artistName}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {

                document.getElementById("artist-name").textContent = data.name;
                document.getElementById("artist-nationality").textContent = data.nationality || "N/A";
                document.getElementById("artist-birthday").textContent = data.birthday || "N/A";
                document.getElementById("artist-deathday").textContent = data.deathday || "N/A";
                document.getElementById("artist-biography").textContent = data.biography || "N/A";
                artistInfo.classList.remove("hidden");
            }
        })
        .catch(error => {
            console.error("Error fetching artist info:", error);
            alert("An error occurred while fetching artist info.");
        })
        .finally(() => {

            loading.classList.add("hidden");
        });
}
