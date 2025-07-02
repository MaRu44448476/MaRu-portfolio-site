// Parallax Effect
document.addEventListener('DOMContentLoaded', () => {
  const parallaxElements = document.querySelectorAll('.parallax-element');
  
  window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    
    parallaxElements.forEach((element, index) => {
      const speed = element.dataset.speed || 0.5;
      const yPos = -(scrolled * speed);
      element.style.transform = `translateY(${yPos}px)`;
    });
  });
});

// Magnetic Effect
document.querySelectorAll('.magnetic-area').forEach(area => {
  const content = area.querySelector('.magnetic-content');
  
  area.addEventListener('mousemove', (e) => {
    const rect = area.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    
    content.style.transform = `translate(${x * 0.1}px, ${y * 0.1}px)`;
  });
  
  area.addEventListener('mouseleave', () => {
    content.style.transform = 'translate(0, 0)';
  });
});

// Page Transition
const pageTransition = document.createElement('div');
pageTransition.className = 'page-transition';
document.body.appendChild(pageTransition);

document.querySelectorAll('a[href^="/"]').forEach(link => {
  link.addEventListener('click', (e) => {
    const href = link.getAttribute('href');
    if (href !== window.location.pathname) {
      e.preventDefault();
      pageTransition.classList.add('active');
      
      setTimeout(() => {
        window.location.href = href;
      }, 500);
    }
  });
});

// Glitch Text Effect
document.querySelectorAll('.glitch').forEach(element => {
  element.setAttribute('data-text', element.textContent);
});

// Scroll Progress Indicator
const createScrollIndicator = () => {
  const sections = document.querySelectorAll('section');
  const indicator = document.createElement('div');
  indicator.className = 'scroll-indicator';
  
  sections.forEach((section, index) => {
    const dot = document.createElement('div');
    dot.className = 'dot';
    dot.addEventListener('click', () => {
      section.scrollIntoView({ behavior: 'smooth' });
    });
    indicator.appendChild(dot);
  });
  
  document.body.appendChild(indicator);
  
  // Update active dot on scroll
  window.addEventListener('scroll', () => {
    const scrollPosition = window.pageYOffset;
    
    sections.forEach((section, index) => {
      const rect = section.getBoundingClientRect();
      const dot = indicator.children[index];
      
      if (rect.top <= window.innerHeight / 2 && rect.bottom >= window.innerHeight / 2) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  });
};

// Initialize scroll indicator
if (document.querySelectorAll('section').length > 1) {
  createScrollIndicator();
}

// Add noise overlay
const noiseOverlay = document.createElement('div');
noiseOverlay.className = 'noise-overlay';
document.body.appendChild(noiseOverlay);

// Text Reveal Animation
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('revealed');
      revealObserver.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.reveal').forEach(element => {
  revealObserver.observe(element);
});