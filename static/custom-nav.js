class Custom_nav extends HTMLElement{

    constructor(){
        super()
    }

    connectedCallback() {
        let shadow = this.attachShadow({ mode: "closed" });
        const style = document.createElement("style");
        style.textContent = `
          nav a {
            text-decoration: none;
            font-family: 'Stock Quote', sans-serif;
            color: #0f0f0f;
            font-size: 25px;
          }
                
          nav  {
            background-color: #ddd;
            padding: 30px;
          }
        `;
        
        const nav = document.createElement("nav");
        const link = document.createElement("a");
        link.setAttribute("id", "gptreino");
        link.setAttribute("href", "/");
        link.textContent = "GPtreino";
    
        nav.appendChild(link);
        
        shadow.appendChild(style);
        shadow.appendChild(nav);
      }

}

customElements.define("custom-nav",Custom_nav);