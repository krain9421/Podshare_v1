$("document").ready(function() {

  function showNotification(message) {
    const notification = document.querySelector(".notification");

    notification.innerHTML = message;
    notification.style.display = "block";
    notification.style.top = "20";

    setTimeout(() => {
      notification.style.top = "-50px";
    }, 5000);
  }

  $("#welcomeMessage").animate({
    opacity: '1'
  }, 2000)

  $("#welcomeTitle").animate({
    opacity: '1'
  }, 2000)

});
