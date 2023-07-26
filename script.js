function toggleDropdown() {
    var dropdownContent = document.getElementById("dropdownContent");
    dropdownContent.style.display = (dropdownContent.style.display === "block") ? "none" : "block";
  }
  
function selectOption(option) {
    document.getElementById("selectedOption").innerText = option;
    toggleDropdown();
  }

  function sendOptionToPython(option) {
    fetch('/process_option', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'selected_option': option })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}