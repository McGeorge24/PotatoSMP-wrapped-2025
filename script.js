async function getStats(file_path) {
    // 1. Wait for the server to send the file
    const response = await fetch(file_path);

    // 2. Wait for the browser to turn the text into a JSON object
    const player = await response.json();
    let hours_played = player.stats["minecraft:custom"]["minecraft:play_time"];
    // 3. Now 'data' is a real object you can use
    console.log(hours_played);
    return hours_played;
}

async function updateUI() {
    const data = await getStats("file.json");
    document.getElementById("value").innerHTML = data;
}

updateUI();