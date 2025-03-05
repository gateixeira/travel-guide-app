document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('itineraryForm');
    const daysInput = document.getElementById('days');
    const daysValue = document.getElementById('daysValue');
    const resultDiv = document.getElementById('result');

    daysInput.addEventListener('input', () => {
        daysValue.textContent = daysInput.value;
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const destination = document.getElementById('destination').value;
        const days = daysInput.value;

        try {
            const response = await fetch('http://localhost:8000/itinerary', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ destination, days: parseInt(days) })
            });

            if (!response.ok) {
                throw new Error('Failed to generate itinerary');
            }

            const data = await response.json();
            displayItinerary(data);
        } catch (error) {
            resultDiv.innerHTML = `<p class="error">Error: ${error.message}</p>`;
        }
    });

    function displayItinerary(data) {
        resultDiv.innerHTML = '';
        let currentDay = null;
        let dayContainer = null;

        data.daily_plans.forEach(item => {
            if (item.startsWith('Day')) {
                if (dayContainer) {
                    resultDiv.appendChild(dayContainer);
                }
                dayContainer = document.createElement('div');
                dayContainer.className = 'day-container';
                
                const dayTitle = document.createElement('h2');
                dayTitle.className = 'day-title';
                dayTitle.textContent = item;
                dayContainer.appendChild(dayTitle);
            } else if (item.trim() && dayContainer) {
                const activityItem = document.createElement('div');
                activityItem.className = 'activity-item';
                activityItem.textContent = item;
                dayContainer.appendChild(activityItem);
            }
        });

        if (dayContainer) {
            resultDiv.appendChild(dayContainer);
        }
    }
});
