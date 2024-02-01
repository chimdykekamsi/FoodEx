      // Product data (an array of products)
      const features = [
        {
            name: "Free Shipping",
            image: "../asset/img/features/f6.png",
       
        },
        {
            name: "Online Order",
            image: "../asset/img/features/f2.png",
        },
        {
            name: "Promotions",
            image: "../asset/img/features/f4.png"
        },
        {
            name: "Happy Selling",
            image: "../asset/img/features/f5.png",
        },
        {
            name: "F24/7 Supportx",
            image: "../asset/img/features/f6.png",
        },
        // Add more features as needed
    ];

    // Access the feature listings container
    const featureContainer = document.querySelector("#feature");

    // Loop through the features and create feature listings
    features.forEach(feature => {
        var featureDiv = document.createElement("div")
        featureDiv.classList.add("feature-box")
        featureContainer.appendChild(featureDiv)

        // feature Image
       var featureImage = document.createElement("img")
        featureImage.src = `${feature.image}`;
        featureImage.alt = "feature Image";
        featureDiv.appendChild(featureImage)

        // feature Name
        var featureName = document.createElement("h6")
        featureName.textContent = feature.name;
        featureDiv.appendChild(featureName)
    

    });

    // About page
    function closeNav(){
        document.getElementById("about").style.width = "0%";
    }
    function openAbout(){
        document.getElementById("about").style.width = "100%";

    }