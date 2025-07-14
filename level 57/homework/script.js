 function handleClick() {
      const input = document.getElementById('myInput');
      const text = input.value;

      console.log("Goa", text);

      const bgColor = prompt("backgroundაგ: red,rgb(253, 113, 164)):");
      if (bgColor) {
        document.body.style.backgroundColor = bgColor;
      }

      input.style.border = "2px solid blue";
      input.style.backgroundColor = "#eef";
    }