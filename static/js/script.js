async function addContact() {
    const name = document.getElementById("name").value;
    const phone = document.getElementById("phone").value;

    if (name && phone) {
        const response = await fetch('/add_contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, phone })
        });
        const result = await response.json();
        alert(result.message);
    } else {
        alert("Please enter both name and phone number.");
    }
}

async function viewBlockchain() {
    const response = await fetch('/view_blockchain');
    const blockchain = await response.json();
    const blockchainDiv = document.getElementById("blockchain");
    blockchainDiv.innerHTML = '';

    blockchain.forEach(block => {
        const blockDiv = document.createElement("div");
        blockDiv.classList.add("block");
        blockDiv.innerHTML = `
            <p><strong>Index:</strong> ${block.index}</p>
            <p><strong>Hash:</strong> ${block.hash}</p>
            <p><strong>Timestamp:</strong> ${new Date(block.timestamp * 1000).toLocaleString()}</p>
            <p><strong>Encrypted Data:</strong> ${JSON.stringify(block.data)}</p>
            <p><strong>Decrypted Name:</strong> ${block.decrypted_data.name}</p>
            <p><strong>Decrypted Phone:</strong> ${block.decrypted_data.phone}</p>
            <p><strong>Previous Hash:</strong> ${block.previous_hash}</p>
        `;
        blockchainDiv.appendChild(blockDiv);
    });
}
