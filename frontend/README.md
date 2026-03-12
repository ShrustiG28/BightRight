# BiteRight - Custom Food Experience 🍽️

A modern, responsive food ordering web application with customizable dishes and an intuitive user interface.

## 🌟 Features

### Core Functionality
- **Custom Food Ordering**: Personalize every dish with ingredient customization
- **Mood-Based Filtering**: Filter dishes by comfort, healthy, cheat meal, or late-night options
- **Real-time Search**: Instant search across dishes and descriptions
- **Interactive Cart**: Dynamic cart with split bill and emergency order features
- **Responsive Design**: Optimized for all devices and screen sizes

### Advanced Features
- **Progressive Web App (PWA)**: Offline functionality with service worker
- **Performance Optimized**: Lazy loading, image optimization, and efficient animations
- **Accessibility**: Keyboard navigation, screen reader support, and high contrast mode
- **Modern UI/UX**: Glassmorphism design with smooth animations and transitions

## 🎨 Design System

### Color Palette
- **Primary**: `#667eea` to `#764ba2` (Purple gradient)
- **Secondary**: `#f093fb` to `#f5576c` (Pink gradient)
- **Success**: `#27ae60` to `#2ecc71` (Green gradient)
- **Warning**: `#feca57` to `#ff9ff3` (Yellow-Pink gradient)
- **Danger**: `#e74c3c` to `#c0392b` (Red gradient)

### Typography
- **Font Family**: Poppins (Google Fonts)
- **Font Weights**: 300, 400, 500, 600, 700
- **Font Sizes**: 0.75rem to 2rem (responsive scaling)

### Spacing System
- **XS**: 0.25rem (4px)
- **SM**: 0.5rem (8px)
- **MD**: 1rem (16px)
- **LG**: 1.5rem (24px)
- **XL**: 2rem (32px)
- **2XL**: 3rem (48px)

## 📁 Project Structure

```
SDC/
├── index.html              # Main homepage
├── style.css              # Core styles
├── design-system.css      # Design system utilities
├── script.js              # Main JavaScript functionality
├── sw.js                  # Service worker for PWA
├── offline.html           # Offline fallback page
├── place-order.html       # Order placement page
├── place-order.css        # Order page styles
├── my-orders.html         # Order history page
├── Customize.html         # Dish customization page
├── ing.html               # Ingredients page
├── 
├── Dish Pages/
│   ├── spicy-biryani.html
│   ├── paneer-butter-masala.html
│   ├── tandoori-chicken.html
│   ├── veg.html
│   ├── Classic-dosa.html
│   ├── mushroom-risotto.html
│   ├── chole-bhature.html
│   ├── thai-green-curry.html
│   ├── chicken-salad.html
│   ├── cheese-pizza.html
│   ├── butter-chicken.html
│   ├── mediterranean-bowl.html
│   ├── ramen-bowl.html
│   ├── quinoa-bowl.html
│   ├── loaded-nachos.html
│   └── fish-curry.html
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Local web server (optional, for development)

### Installation
1. Clone or download the project files
2. Open `index.html` in your web browser
3. For development, use a local server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx serve .
   
   # Using PHP
   php -S localhost:8000
   ```

### Development Setup
1. Install a code editor (VS Code recommended)
2. Install Live Server extension for real-time preview
3. Open the project folder in your editor
4. Start Live Server to begin development

## 🎯 Usage

### Navigation
- **Home**: Browse all available dishes
- **Search**: Use the search bar to find specific dishes
- **Mood Filters**: Click mood buttons to filter dishes
- **Dish Pages**: Click "CUSTOMIZE NOW" to personalize dishes
- **Cart**: Review and manage your orders
- **Orders**: View order history

### Customization
1. Select a dish from the homepage
2. Choose/uncheck ingredients on the dish page
3. Adjust spice levels, protein choices, or sizes (where available)
4. See real-time price updates
5. Proceed to customization for final order

### Keyboard Shortcuts
- **Ctrl/Cmd + K**: Focus search bar
- **Ctrl/Cmd + R**: Reset all filters
- **/**: Quick search focus

## 🛠️ Technical Details

### Technologies Used
- **HTML5**: Semantic markup and structure
- **CSS3**: Modern styling with custom properties
- **JavaScript (ES6+)**: Interactive functionality
- **Service Worker**: PWA capabilities
- **Intersection Observer**: Performance optimizations
- **CSS Grid & Flexbox**: Responsive layouts

### Performance Features
- **Lazy Loading**: Images load as needed
- **Debounced Search**: Optimized search performance
- **Efficient Animations**: GPU-accelerated transforms
- **Caching Strategy**: Service worker caching
- **Image Optimization**: Responsive images with Unsplash

### Browser Support
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 🎨 Design Principles

### Visual Design
- **Glassmorphism**: Translucent elements with backdrop blur
- **Gradient Backgrounds**: Dynamic color transitions
- **Micro-interactions**: Subtle hover and click animations
- **Consistent Spacing**: Systematic spacing scale
- **Typography Hierarchy**: Clear content structure

### User Experience
- **Progressive Enhancement**: Works without JavaScript
- **Mobile-First**: Responsive design approach
- **Accessibility**: WCAG 2.1 AA compliance
- **Performance**: Fast loading and smooth interactions
- **Offline Support**: Works without internet connection

## 📱 Responsive Breakpoints

- **Mobile**: 320px - 480px
- **Tablet**: 481px - 768px
- **Desktop**: 769px - 1200px
- **Large Desktop**: 1201px+

## 🔧 Customization

### Adding New Dishes
1. Create a new HTML file in the project root
2. Copy the structure from an existing dish page
3. Update the dish information and ingredients
4. Add the dish card to `index.html`
5. Update the service worker cache list

### Modifying Styles
1. Use CSS custom properties in `:root` for global changes
2. Utilize utility classes from `design-system.css`
3. Follow the existing naming conventions
4. Test across all breakpoints

### Adding Features
1. Follow the existing JavaScript patterns
2. Use event delegation for dynamic content
3. Implement proper error handling
4. Update the service worker if needed

## 🚀 Deployment

### Static Hosting
- **Netlify**: Drag and drop deployment
- **Vercel**: Git-based deployment
- **GitHub Pages**: Free hosting for public repos
- **Firebase Hosting**: Google's hosting solution

### Build Process
No build process required - this is a vanilla web application that runs directly in the browser.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test across different devices
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Unsplash**: High-quality food images
- **Google Fonts**: Poppins font family
- **CSS Tricks**: Design inspiration and techniques
- **MDN Web Docs**: Technical documentation

## 📞 Support

For support, questions, or suggestions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

---

**BiteRight** - Eat what you want, avoid what you don't! 🍽️