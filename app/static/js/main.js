const loader = document.getElementById("loader");
const cards = document.getElementById("cards");
const searchLoader=document.getElementById("search-loader");
const searchProduct = document.getElementById("search-product");
const secondSearchProduct = document.getElementById("second-search-product");
const secondSearchLoader = document.getElementById("second-search-loader");
const bars =document.getElementById("bars");



fetch("/products")
.then(response => response.json())
.then(products =>{  
    loader.style.display="none";  
    products.forEach(product => {

        let card = document.createElement("div")
        card.classList.add("card")
        card.innerHTML=`
        <img src="static/product_images/${product.image}" alt="${product.name}">
        
        <div class="desc"> 
        ${product.desc} 
        <strong>$${product.price}</strong>
        </div>
        `;

        cards.appendChild(card)

    });
});

function secondSearch(){
    secondSearchLoader.style.display = 'block';
    secondSearchProduct.style.display = 'none';
    
}
function search(){
        searchLoader.style.display='block';
        searchProduct.style.display='none';
}

function toggleBar(){
    bars.classList.toggle("fa-bars");
    bars.classList.toggle("fa-times");
    
}

