<html><head><base href="https://gpt.com/chat/axios.js/gpt-3.5">
<title>GPT-3.5 Chat Interface</title>
<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f0f0f0;
  }
  #chat-container {
    max-width: 800px;
    margin: 20px auto;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    overflow: hidden;
  }
  #chat-messages {
    height: 400px;
    overflow-y: auto;
    padding: 20px;
  }
  .message {
    margin-bottom: 15px;
    padding: 10px;
    border-radius: 5px;
  }
  .user-message {
    background-color: #e6f2ff;
    text-align: right;
  }
  .bot-message {
    background-color: #f0f0f0;
  }
  #user-input {
    display: flex;
    padding: 20px;
    background-color: #f9f9f9;
  }
  #user-input input {
    flex-grow: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  #user-input button {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    margin-left: 10px;
    cursor: pointer;
  }
</style>
</head>
<body>
<div id="chat-container">
  <div id="chat-messages"></div>
  <div id="user-input">
    <input type="text" id="message-input" placeholder="Type your message...">
    <button onclick="sendMessage()">Send</button>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
const chatMessages = document.getElementById('chat-messages');
const messageInput = document.getElementById('message-input');

async function sendMessage() {
  const userMessage = messageInput.value.trim();
  if (userMessage === '') return;

  addMessage('user', userMessage);
  messageInput.value = '';

  try {
    const response = await axios.post('/api/chat', { message: userMessage });
    const botReply = response.data.reply;
    addMessage('bot', botReply);
  } catch (error) {
    console.error('Error:', error);
    addMessage('bot', 'Sorry, I encountered an error. Please try again.');
  }
}

function addMessage(sender, text) {
  const messageElement = document.createElement('div');
  messageElement.classList.add('message', `${sender}-message`);
  messageElement.textContent = text;
  chatMessages.appendChild(messageElement);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

messageInput.addEventListener('keypress', function(event) {
  if (event.key === 'Enter') {
    sendMessage();
  }
});

// Initial greeting
addMessage('bot', 'Hello! I\'m GPT-3.5. How can I assist you today?');
</script>
</body></html>