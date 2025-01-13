// Fungsi untuk animasi Gradient Descent
const animateGradientDescent = (positions) => {
    // Buat scatter plot dengan Plotly
    const trace1 = {
        x: positions.map(p => p.m),
        y: positions.map(p => p.c),
        mode: 'lines+markers',
        type: 'scatter'
    };

    const layout = {
        title: 'Gradient Descent Path',
        xaxis: { title: 'm (slope)' },
        yaxis: { title: 'c (intercept)' }
    };

    Plotly.newPlot('chart', [trace1], layout);

    // Animasi bola bergerak di jalur descent
    let i = 0;
    const interval = setInterval(() => {
        if (i < positions.length) {
            const update = {
                x: [[positions[i].m]],
                y: [[positions[i].c]]
            };
            Plotly.extendTraces('chart', update, [0]);
            i++;
        } else {
            clearInterval(interval);
        }
    }, 500);
};

// Fungsi onsubmit untuk form
document.getElementById('grad-form').onsubmit = async (e) => {
    e.preventDefault();

    // Ambil input dari form
    const dataInput = JSON.parse(document.getElementById('data').value);
    const learningRate = parseFloat(document.getElementById('learning_rate').value);
    const iterations = parseInt(document.getElementById('iterations').value);

    try {
        // Kirim request ke API Flask
        const response = await fetch('/compute', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                data: dataInput,
                initial_line: [0, 0], // default nilai awal
                learning_rate: learningRate,
                iterations: iterations,
            }),
        });

        const result = await response.json();

        // Tampilkan hasil akhir (final line) di halaman
        document.getElementById('output').innerHTML = `
            <p><strong>Final Line:</strong> y = ${result.m.toFixed(4)}x + ${result.c.toFixed(4)}</p>
        `;

        // Jalankan animasi Gradient Descent
        const positions = result.positions; // Ambil history posisi dari API
        animateGradientDescent(positions);

    } catch (error) {
        console.error('Error fetching data:', error);
        document.getElementById('output').innerHTML = `
            <p style="color: red;">Error: Unable to fetch data. Please check your input and try again.</p>
        `;
    }
};
