
import io

with io.open(r'd:\1\quick-order\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find bottom nav
start_nav = html.find('<!-- BOTTOM NAV -->')
end_nav = html.find('</div>', html.find('</nav>')) + 6
nav_html = html[start_nav:end_nav]

# find full products modal
start_modal = html.find('<!-- ===== FULL PRODUCTS MODAL ===== -->')
end_modal = html.find('</div>', html.find('id=\"fullProductsBody\"')) + 6
modal_html = html[start_modal:end_modal]

# replace them in the original html
html = html.replace(nav_html, '')
html = html.replace(modal_html, '')

# find the closing of main-content (which is before MODALS)
modals_start = html.find('<!-- ===== MODALS ===== -->')
html = html[:modals_start] + modal_html + '\n\n' + nav_html + '\n\n' + html[modals_start:]

with io.open(r'd:\1\quick-order\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')

