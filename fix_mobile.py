import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add the "Xem thêm" button right after the flex-gallery
gallery_end_idx = html.find('</div>\n      </div>\n    </section>\n\n    <!-- 07 CLOSING -->')
if gallery_end_idx == -1:
    print("Could not find end of gallery")
    sys.exit(1)

btn_html = '''        <div class="text-center" style="margin-top: 32px;">
          <button id="btn-show-more" class="button" style="display: none; background: transparent; color: var(--ink);" onclick="showMoreGallery()">Xem thêm báo cáo &darr;</button>
        </div>
'''
html = html[:gallery_end_idx] + btn_html + html[gallery_end_idx:]

# 2. Rewrite JS logic
js_start_idx = html.find('// Industry Filter Logic')
js_end_idx = html.find('const menuButton = document.querySelector(\'.menu-button\');')

new_js = '''// Gallery State & Event Delegation
    let currentIndustry = 'all';
    let isMobileCollapsed = true;
    const MOBILE_LIMIT = 4;
    const flexGallery = document.getElementById('flex-gallery');

    flexGallery.addEventListener('click', (e) => {
      if(e.target.tagName === 'IMG') {
        const visibleImages = Array.from(flexGallery.querySelectorAll('img:not(.hidden)'));
        const index = visibleImages.indexOf(e.target);
        if(index > -1) {
          currentGallery = visibleImages;
          currentIndex = index;
          openLightbox();
        }
      }
    });

    function renderGallery() {
      const isMobile = window.innerWidth <= 768;
      const images = flexGallery.querySelectorAll('img');
      let matchCount = 0;

      images.forEach(img => {
        const matches = (currentIndustry === 'all' || img.dataset.industry === currentIndustry);
        if (matches) {
          matchCount++;
          if (isMobile && isMobileCollapsed && matchCount > MOBILE_LIMIT) {
            img.classList.add('hidden');
          } else {
            img.classList.remove('hidden');
          }
        } else {
          img.classList.add('hidden');
        }
      });

      const btnMore = document.getElementById('btn-show-more');
      if (btnMore) {
        if (isMobile && isMobileCollapsed && matchCount > MOBILE_LIMIT) {
          btnMore.style.display = 'inline-flex';
        } else {
          btnMore.style.display = 'none';
        }
      }
    }

    function filterIndustry(ind, event) {
      if (event) {
        document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
        event.target.classList.add('active');
      }
      currentIndustry = ind;
      isMobileCollapsed = true;
      renderGallery();
    }

    function showMoreGallery() {
      isMobileCollapsed = false;
      renderGallery();
    }

    let resizeTimer;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(renderGallery, 150);
    });

    document.addEventListener('DOMContentLoaded', () => {
      renderGallery();
    });

    '''

html = html[:js_start_idx] + new_js + html[js_end_idx:]

# Also remove the old lightbox loop that initialized events for .proof-gallery
old_lb_init = '''document.querySelectorAll('.proof-gallery').forEach(gallery => {
      const images = Array.from(gallery.querySelectorAll('img'));
      images.forEach((img, index) => {
        img.addEventListener('click', () => {
          currentGallery = images;
          currentIndex = index;
          openLightbox();
        });
      });
    });'''

new_lb_init = '''document.querySelectorAll('.proof-gallery:not(#flex-gallery)').forEach(gallery => {
      gallery.addEventListener('click', (e) => {
        if(e.target.tagName === 'IMG') {
          const images = Array.from(gallery.querySelectorAll('img'));
          const index = images.indexOf(e.target);
          if(index > -1) {
            currentGallery = images;
            currentIndex = index;
            openLightbox();
          }
        }
      });
    });'''

html = html.replace(old_lb_init, new_lb_init)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated successfully")
