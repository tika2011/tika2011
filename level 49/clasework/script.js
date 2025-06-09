     document.getElementById("message").innerHTML = "hallo this page.";

       
        let city = "batumi";  
        let population = 1200000;    
        let isCapital = true;       

        console.log("city:", city);
        console.log("population:", population);
        console.log("capital:", isCapital);
        document.getElementById("internalBtn").onclick = function() {
            alert("Internal JS clik !");
        }
        function inlineExample() {
            alert("ეს არის Inline JS!");
        }