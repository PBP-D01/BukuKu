async function getProducts() {
    try {
        const response = await fetch("{% url 'leaderboard:get_product_json' %}");
        if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const products = await response.json();
        
        // Sort the products by the 'buys' attribute in ascending order
        products.sort((a, b) => a.buys - b.buys);
        
        return products;
    } catch (error) {
        console.error("Error fetching and sorting products:", error);
        throw error;
    }
}


async function refreshProducts() {
    document.getElementById("product_table").innerHTML = ""
    const products = await getProducts()
    products.sort((a, b) => b.buys - a.buys);
    let htmlString = `<tr>
        <th>Rank</th>
        <th>Title</th>
        <th>Price</th>
        <th>Author</th>
        <th>Stars</th>
        <th>Buys</th>
    </tr>`
    var rank = 0
    products.forEach((item) => {
        rank +=1
        htmlString += `\n<tr>
        <td>${rank}</td>
        <td>${item.fields.title}</td>
        <td>${item.fields.price}</td>
        <td>${item.fields.author}</td>
        <td>${item.fields.stars}</td>
        <td>${item.fields.buys}</td>
    </tr>` 
    })


    document.getElementById("product_table").innerHTML = htmlString
}

refreshProducts()

async function filter(input){
document.getElementById("product_table").innerHTML = ""
    const products = await getProducts()
    products.sort((a, b) => b.buys - a.buys);
    let htmlString = `<tr>
        <th>Rank</th>
        <th>Title</th>
        <th>Price</th>
        <th>Author</th>
        <th>Stars</th>
        <th>Buys</th>
    </tr>`
    var rank = 0
    products.forEach((item) => {
        rank +=1
        if(item.fields.title.toLowerCase().includes(input.value.toLowerCase())){
        htmlString += `\n<tr>
        <td>${rank}</td>
        <td>${item.fields.title}</td>
        <td>${item.fields.price}</td>
        <td>${item.fields.author}</td>
        <td>${item.fields.stars}</td>
        <td>${item.fields.buys}</td>
        </tr>` 
        }
        
    })


    document.getElementById("product_table").innerHTML = htmlString
}
