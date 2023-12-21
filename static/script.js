function playGame(choice) {
    // Afficher le choix de l'ordinateur avant de faire la requête AJAX
    const resultContainer = document.getElementById('result');
    resultContainer.innerText = `L'ordinateur choisit...`;
    
    fetch('/play', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: 'choice=' + choice,
    })
    .then(response => response.json())
    .then(data => {
      // Gérer la réponse JSON
      updateUI(data);
    })
    .catch(error => {
      console.error('Erreur lors de la requête:', error);
    });
  }
  
  function updateUI(data) {
    // Mettez à jour le résultat, les points et le choix de l'ordinateur
    document.getElementById('result').innerText = data.result;
    document.getElementById('Pointsjoueur').innerText = data.Pointsjoueur;
    document.getElementById('Pointsordinateur').innerText = data.Pointsordinateur;
    document.getElementById('computer-choice').innerText = `L'ordinateur a choisi : ${data.ordinateur}`;
}

  
  

