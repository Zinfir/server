const Product_Category = ({name}) => (
    `<li class="menu__item">
        <h2>
            ${name}
        </h2>
    </li>`
)

const renderData = res => {
    menuHtml = res.data.results.map(Product_Category)
        .join('')
    menu = document.getElementById('rest_menu')
    menu.innerHTML += menuHtml
}