document.addEventListener("DOMContentLoaded", () => {
  document.querySelector("#form").onsubmit = () => {
    // Initialize new request
    const request = new XMLHttpRequest();
    const from = document.querySelector("#from").value;
    const to = document.querySelector("#to").value;
    request.open("POST", "/convert");

    // Callback function for when request completes
    request.onload = () => {
      // Extract JSON data from request
      const data = JSON.parse(request.responseText);
      console.log(data);
      // Update the result div
      const contents = `1 ${from} is equal to ${data.rate} ${to}`;
      document.querySelector("#result").innerHTML = contents;
    };

    // Add data to send with request
    const data = new FormData();
    data.append("from", from);
    data.append("to", to);

    // Send request
    request.send(data);
    return false;
  };
});
