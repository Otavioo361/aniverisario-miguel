const params = new URLSearchParams(window.location.search);
const nome = params.get("nome");
const codigo = params.get("codigo");

if (nome) {
  document.getElementById("nomeConvidado").innerText = `Olá, ${nome}!`;
}

function responder(resposta) {
  const url = "https://script.google.com/macros/s/AKfycbxK6WlfYm82LUz-wIbSIVZDb3zhr9XdIcwK3rntPiTDUR3i4QgqbHQuX9wwDuB1zSPU/exec";
  fetch(`${url}?nome=${encodeURIComponent(nome)}&codigo=${codigo}&resposta=${resposta}`)
    .then(res => res.text())
    .then(msg => {
      document.getElementById("mensagem").innerText = msg;
    })
    .catch(err => {
      document.getElementById("mensagem").innerText = "Erro ao enviar resposta.";
      console.error(err);
    });
}