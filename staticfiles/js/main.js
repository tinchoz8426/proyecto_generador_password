function myFunction() {
    /* Get the text field */
    let copyText = document.getElementById("myInput");
    let messageCopied = document.getElementById("message-copied")

    let copyMessage = "<p style='color: white; margin: 1rem 0 0 0'>¡Texto copiado!</p>"

     /* Copy the text inside the text field */
    navigator.clipboard.writeText(copyText.innerText);
    messageCopied.innerHTML = copyMessage

    setTimeout(() => {
        messageCopied.style.display = "none"
    }, 2000);

    messageCopied.style.display = "block"
  }