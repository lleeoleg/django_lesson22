const domain = 'http://localhost:8000/api/';

const list = document.querySelector('#list');

async function loadList() {
    const result = await fetch(`${domain}rubrics`);
    if (result.ok) {
        const data = await result.json();
        let s = '', d;
        for (let i = 0; i < data.length; i++) {
            d = data[i];
            s += `<li>${d.name} <a href="${domain}rubrics/${d.id}/" class="detail">Вывести</a></li>`;
        }
        list.innerHTML = s;
        
        let links = list.querySelectorAll('li a.detail');
        links.forEach((link) => {
            link.addEventListener('click', loadItem);
        });

    } else {
        window.console.log(result.statusText);
    }
}

loadList();
