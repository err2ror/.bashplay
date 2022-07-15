// Import stylesheets
import './style.css';
import "./index.html"
// Write Javascript code!
const app = document.getElementById("app")
function execute(){
  return "<p>hello</p>"
}
app.innerHTML = execute()