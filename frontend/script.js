// Enhanced JavaScript for BiteRight App

// DOM Elements - Using a function to ensure elements are accessed after DOM is loaded
let searchBar, moodButtons, restaurantCards, loadingOverlay, navButtons;

function initializeDOMElements() {
    searchBar = document.getElementById('searchBar');
    moodButtons = document.querySelectorAll('.mood-btn');
    restaurantCards = document.querySelectorAll('.restaurant-card');
    loadingOverlay = document.getElementById('loadingOverlay');
    navButtons = document.querySelectorAll('.nav-btn');
    
    // Log elements to check if they're properly selected
    console.log('Loading overlay:', loadingOverlay);
    console.log('Search bar:', searchBar);
}

// App State
let currentFilter = 'all';
let searchTerm = '';
let isLoading = false;

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
    // Initialize DOM elements first
    initializeDOMElements();
    
    // Then proceed with other initializations
    initializeApp();
    setupEventListeners();
    animateCards();
    setupPerformanceOptimizations();
    
    console.log('App initialized successfully');
});

function initializeApp() {
    // Show loading animation briefly
    showLoading();
    setTimeout(() => {
        hideLoading();
    }, 1500);
}

function setupEventListeners() {
    // Search functionality
    searchBar.addEventListener('input', handleSearch);
    
    // Mood filter functionality
    moodButtons.forEach(button => {
        button.addEventListener('click', handleMoodFilter);
    });
    
    // Cart functionality
    document.getElementById("splitBill").addEventListener('click', handleSplitBill);
    document.getElementById("quickOrder").addEventListener('click', handleQuickOrder);
    
    // Navigation functionality
    navButtons.forEach(button => {
        button.addEventListener('click', handleNavigation);
    });
    
    // Card hover effects
    restaurantCards.forEach(card => {
        card.addEventListener('mouseenter', handleCardHover);
        card.addEventListener('mouseleave', handleCardLeave);
    });
}

// Original search function (will be replaced by enhanced version below)
function _handleSearch(event) {
    const searchTerm = event.target.value.toLowerCase();
    
    restaurantCards.forEach(card => {
        const dishName = card.querySelector('h2').textContent.toLowerCase();
        const description = card.querySelector('p').textContent.toLowerCase();
        
        if (dishName.includes(searchTerm) || description.includes(searchTerm)) {
            card.style.display = 'block';
            card.classList.add('visible');
            card.classList.remove('hidden');
        } else {
            card.classList.add('hidden');
            card.classList.remove('visible');
            setTimeout(() => {
                if (card.classList.contains('hidden')) {
                    card.style.display = 'none';
                }
            }, 300);
        }
    });
}

// Original mood filter function (will be replaced by enhanced version below)
function _handleMoodFilter(event) {
    const selectedMood = event.target.dataset.mood;
    
    // Update active button
    moodButtons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    
    // Filter cards based on mood
    restaurantCards.forEach(card => {
        const categories = card.dataset.category.split(' ');
        
        if (selectedMood === 'comfort' && categories.includes('comfort')) {
            showCard(card);
        } else if (selectedMood === 'healthy' && categories.includes('healthy')) {
            showCard(card);
        } else if (selectedMood === 'cheat' && categories.includes('cheat')) {
            showCard(card);
        } else if (selectedMood === 'late-night' && (categories.includes('comfort') || categories.includes('cheat'))) {
            showCard(card);
        } else {
            hideCard(card);
        }
    });
    
    // Show loading animation
    showLoading();
    setTimeout(hideLoading, 800);
}

function showCard(card) {
    card.style.display = 'block';
    setTimeout(() => {
        card.classList.add('visible');
        card.classList.remove('hidden');
    }, 50);
}

function hideCard(card) {
    card.classList.add('hidden');
    card.classList.remove('visible');
    setTimeout(() => {
        if (card.classList.contains('hidden')) {
            card.style.display = 'none';
        }
    }, 300);
}

function handleSplitBill() {
    showNotification("💳 Split-the-bill feature coming soon!", "info");
}

function handleQuickOrder() {
    showLoading();
    setTimeout(() => {
        hideLoading();
        showNotification("⚡ Your emergency order has been placed! ETA: 15-20 minutes", "success");
    }, 2000);
}

function handleNavigation(event) {
    const targetPage = event.currentTarget.dataset.page;
    
    // Update active navigation
    navButtons.forEach(btn => btn.classList.remove('active'));
    event.currentTarget.classList.add('active');
    
    // Add navigation feedback
    if (targetPage !== 'home') {
        showNotification(`🚀 Navigating to ${targetPage}...`, "info");
    }
}

function handleCardHover(event) {
    const card = event.currentTarget;
    const img = card.querySelector('img');
    
    // Add subtle animation
    card.style.transform = 'translateY(-8px) scale(1.02)';
}

function handleCardLeave(event) {
    const card = event.currentTarget;
    
    // Reset animation
    card.style.transform = 'translateY(0) scale(1)';
}

function animateCards() {
    restaurantCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            card.style.transition = 'all 0.6s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
}

function showLoading() {
    loadingOverlay.classList.add('show');
}

function hideLoading() {
    loadingOverlay.classList.remove('show');
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    // Style the notification
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? 'linear-gradient(135deg, #27ae60, #2ecc71)' : 
                     type === 'error' ? 'linear-gradient(135deg, #e74c3c, #c0392b)' : 
                     'linear-gradient(135deg, #667eea, #764ba2)'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
        z-index: 10000;
        font-weight: 500;
        max-width: 300px;
        transform: translateX(400px);
        transition: transform 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Remove after delay
    setTimeout(() => {
        notification.style.transform = 'translateX(400px)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Add smooth scrolling for better UX
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add keyboard navigation
document.addEventListener('keydown', function(event) {
    if (event.key === '/') {
        event.preventDefault();
        searchBar.focus();
    }
});

// Add intersection observer for scroll animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for scroll animations
document.querySelectorAll('.restaurant-card, .cart').forEach(el => {
    observer.observe(el);
});

// Performance optimizations
function setupPerformanceOptimizations() {
    // Lazy load images
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src || img.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });

    // Debounce search function
    let searchTimeout;
    const originalHandleSearch = handleSearch;
    
    // Replace the handleSearch function with a debounced version
    const debouncedHandleSearch = function(event) {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            originalHandleSearch(event);
        }, 300);
    };
    
    // Update the event listener to use the debounced function
    searchBar.removeEventListener('input', handleSearch);
    searchBar.addEventListener('input', debouncedHandleSearch);
}

// Enhanced filter functionality
function applyFilters() {
    restaurantCards.forEach(card => {
        const categories = card.dataset.category.split(' ');
        const dishName = card.querySelector('h2').textContent.toLowerCase();
        const description = card.querySelector('p').textContent.toLowerCase();
        
        const matchesSearch = searchTerm === '' || 
                            dishName.includes(searchTerm) || 
                            description.includes(searchTerm);
        
        const matchesFilter = currentFilter === 'all' || 
                            (currentFilter === 'comfort' && categories.includes('comfort')) ||
                            (currentFilter === 'healthy' && categories.includes('healthy')) ||
                            (currentFilter === 'cheat' && categories.includes('cheat')) ||
                            (currentFilter === 'late-night' && (categories.includes('comfort') || categories.includes('cheat')));
        
        if (matchesSearch && matchesFilter) {
            showCard(card);
        } else {
            hideCard(card);
        }
    });
}

// Analytics tracking (placeholder for future implementation)
function trackEvent(eventName, properties = {}) {
    console.log(`Event: ${eventName}`, properties);
    // Here you would integrate with your analytics service
}

// Enhanced mood filter with state management
function handleMoodFilter(event) {
    const selectedMood = event.target.dataset.mood;
    currentFilter = selectedMood;
    
    // Update active button
    moodButtons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    
    // Apply filters
    applyFilters();
    
    // Show loading animation
    showLoading();
    setTimeout(hideLoading, 800);
    
    // Analytics tracking (placeholder)
    trackEvent('mood_filter_used', { mood: selectedMood });
}

// Enhanced search with state management
function handleSearch(event) {
    searchTerm = event.target.value.toLowerCase();
    applyFilters();
}

// Add "Show All" functionality
function showAllCards() {
    currentFilter = 'all';
    searchTerm = '';
    searchBar.value = '';
    
    moodButtons.forEach(btn => btn.classList.remove('active'));
    
    restaurantCards.forEach(card => {
        showCard(card);
    });
}

// Add reset filters button functionality
function addResetButton() {
    const resetButton = document.createElement('button');
    resetButton.className = 'mood-btn';
    resetButton.textContent = '🔄 Show All';
    resetButton.addEventListener('click', showAllCards);
    
    const moodFilters = document.querySelector('.mood-filters');
    moodFilters.appendChild(resetButton);
}

// Analytics tracking function has been moved above

// Enhanced error handling
function handleError(error, context = '') {
    console.error(`Error in ${context}:`, error);
    showNotification(`❌ Something went wrong. Please try again.`, 'error');
}

// Add service worker for offline functionality (placeholder)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}

// Initialize enhanced features
document.addEventListener('DOMContentLoaded', function() {
    addResetButton();
    
    // Add keyboard shortcuts
    document.addEventListener('keydown', function(event) {
        if (event.ctrlKey || event.metaKey) {
            switch(event.key) {
                case 'k':
                    event.preventDefault();
                    searchBar.focus();
                    break;
                case 'r':
                    event.preventDefault();
                    showAllCards();
                    break;
            }
        }
    });
    
    // Add touch gestures for mobile
    let touchStartY = 0;
    document.addEventListener('touchstart', function(event) {
        touchStartY = event.touches[0].clientY;
    });
    
    document.addEventListener('touchend', function(event) {
        const touchEndY = event.changedTouches[0].clientY;
        const diff = touchStartY - touchEndY;
        
        // Pull to refresh gesture
        if (diff < -100 && window.scrollY === 0) {
            showLoading();
            setTimeout(() => {
                hideLoading();
                showNotification('🔄 Content refreshed!', 'success');
            }, 1500);
        }
    });
});
  