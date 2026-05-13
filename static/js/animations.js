/**
 * Zenelait Infotech Animation Engine
 * Handles scroll reveal animations and micro-interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    // Initialize Scroll Reveal
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                // Stop observing once animated
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Target all elements with reveal classes
    const animatedElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
    
    animatedElements.forEach(el => {
        observer.observe(el);
    });

    // Optional: Parallax effect on hero banner background
    const hero = document.querySelector('.hero');
    if (hero) {
        window.addEventListener('scroll', () => {
            const scrollPosition = window.pageYOffset;
            hero.style.backgroundPositionY = scrollPosition * 0.5 + 'px';
        });
    }

    // --- NEW: Dynamic Content Features ---

    // 1. Auto-Typing Feature for Hero
    const typedSpan = document.querySelector('.typed-text');
    if (typedSpan) {
        const words = JSON.parse(typedSpan.dataset.words || '[]');
        let wordIndex = 0;
        let charIndex = 0;
        let isDeleting = false;

        function type() {
            const currentWord = words[wordIndex];
            
            if (isDeleting) {
                charIndex--;
            } else {
                charIndex++;
            }

            typedSpan.textContent = currentWord.substring(0, charIndex);

            let typeSpeed = isDeleting ? 50 : 150;

            if (!isDeleting && charIndex === currentWord.length) {
                typeSpeed = 2000; // Pause at end
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                wordIndex = (wordIndex + 1) % words.length;
                typeSpeed = 500;
            }

            setTimeout(type, typeSpeed);
        }

        if (words.length > 0) {
            setTimeout(type, 1000);
        }
    }

    // 2. Counter Increment Animation
    const statsCounters = document.querySelectorAll('.stat-number');
    
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;
                const limit = parseInt(target.dataset.target, 10);
                let current = 0;
                const duration = 2000; // 2 seconds
                const increment = limit / (duration / 16); // roughly 60fps

                const updateCounter = () => {
                    current += increment;
                    if (current < limit) {
                        target.innerText = Math.ceil(current);
                        requestAnimationFrame(updateCounter);
                    } else {
                        target.innerText = limit;
                    }
                };
                updateCounter();
                counterObserver.unobserve(target);
            }
        });
    }, { threshold: 0.5 });

    statsCounters.forEach(cnt => counterObserver.observe(cnt));
});
