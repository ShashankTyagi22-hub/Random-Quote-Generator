const quoteElement = document.getElementById("quote");
const authorElement = document.getElementById("author");
const newButton = document.getElementById("newQuote");
const copyButton = document.getElementById("copyQuote");
const shareButton = document.getElementById("shareQuote");
const favoriteButton = document.getElementById("favoriteQuote");
const message = document.getElementById("message");
const favoritesList = document.getElementById("favoritesList");
const favoriteCount = document.getElementById("favoriteCount");

let currentQuote = null;
let savedQuotes = [];

try {
    savedQuotes = JSON.parse(
        localStorage.getItem("quotespaceFavorites") || "[]"
    );
    if (!Array.isArray(savedQuotes)) savedQuotes = [];
} catch {
    savedQuotes = [];
}

function quoteKey(q) {
    return q.text + " — " + q.author;
}

function showMessage(text) {
    message.textContent = text;
}

function updateFavoriteButton() {
    if (!currentQuote) return;

    const exists = savedQuotes.some(
        q => quoteKey(q) === quoteKey(currentQuote)
    );

    favoriteButton.textContent = exists ? "♥ Saved" : "♡ Favorite";
}

async function getQuote() {
    newButton.disabled = true;
    showMessage("");

    try {
        const response = await fetch("/api/quote");
        if (!response.ok) throw new Error("Request failed");

        currentQuote = await response.json();
        quoteElement.textContent = '"' + currentQuote.text + '"';
        authorElement.textContent = "— " + currentQuote.author;
        updateFavoriteButton();
    } catch {
        showMessage("Could not load a quote. Please try again.");
    } finally {
        newButton.disabled = false;
    }
}

async function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(text);
        return;
    }

    const area = document.createElement("textarea");
    area.value = text;
    area.style.position = "fixed";
    area.style.opacity = "0";
    document.body.appendChild(area);
    area.select();

    const copied = document.execCommand("copy");
    area.remove();

    if (!copied) throw new Error("Copy failed");
}

newButton.addEventListener("click", getQuote);

copyButton.addEventListener("click", async () => {
    if (!currentQuote) return;

    try {
        await copyText('"' + currentQuote.text + '" — ' + currentQuote.author);
        showMessage("Quote copied to clipboard!");
    } catch {
        showMessage("Copy failed. Please select and copy the quote.");
    }
});

shareButton.addEventListener("click", async () => {
    if (!currentQuote) return;

    const text = '"' + currentQuote.text + '" — ' + currentQuote.author;

    if (navigator.share) {
        try {
            await navigator.share({ title: "QuoteSpace", text });
            showMessage("Share menu opened.");
        } catch (error) {
            if (error.name !== "AbortError") {
                showMessage("Unable to share this quote.");
            }
        }
    } else {
        const url = "https://wa.me/?text=" + encodeURIComponent(text);
        window.open(url, "_blank", "noopener,noreferrer");
    }
});

favoriteButton.addEventListener("click", () => {
    if (!currentQuote) return;

    const key = quoteKey(currentQuote);
    const exists = savedQuotes.some(q => quoteKey(q) === key);

    if (exists) {
        savedQuotes = savedQuotes.filter(q => quoteKey(q) !== key);
        showMessage("Removed from favorites.");
    } else {
        savedQuotes.push({ ...currentQuote });
        showMessage("Added to favorites!");
    }

    localStorage.setItem("quotespaceFavorites", JSON.stringify(savedQuotes));
    renderFavorites();
    updateFavoriteButton();
});

function renderFavorites() {
    favoriteCount.textContent =
        savedQuotes.length + (savedQuotes.length === 1 ? " saved" : " saved");

    favoritesList.replaceChildren();

    if (savedQuotes.length === 0) {
        const empty = document.createElement("p");
        empty.className = "empty";
        empty.textContent = "Your favorite quotes will appear here.";
        favoritesList.appendChild(empty);
        return;
    }

    savedQuotes.forEach(q => {
        const card = document.createElement("article");
        card.className = "favorite-card";

        const text = document.createElement("p");
        text.textContent = '"' + q.text + '"';

        const author = document.createElement("p");
        author.className = "favorite-author";
        author.textContent = "— " + q.author;

        const copy = document.createElement("button");
        copy.textContent = "📋 Copy";
        copy.addEventListener("click", async () => {
            try {
                await copyText('"' + q.text + '" — ' + q.author);
                showMessage("Favorite quote copied!");
            } catch {
                showMessage("Unable to copy quote.");
            }
        });

        const remove = document.createElement("button");
        remove.textContent = "Remove";
        remove.addEventListener("click", () => {
            savedQuotes = savedQuotes.filter(
                item => quoteKey(item) !== quoteKey(q)
            );
            localStorage.setItem(
                "quotespaceFavorites",
                JSON.stringify(savedQuotes)
            );
            renderFavorites();
            updateFavoriteButton();
            showMessage("Favorite removed.");
        });

        card.append(text, author, copy, remove);
        favoritesList.appendChild(card);
    });
}

renderFavorites();
getQuote();