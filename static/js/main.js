/* main.js — Interactivity for Amrita CSE Navigator */

document.addEventListener('DOMContentLoaded', function () {
    // Sidebar Toggle for mobile
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('sidebar');
    const mainWrapper = document.querySelector('.main-wrapper');

    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function () {
            sidebar.classList.toggle('active');
            if (mainWrapper) mainWrapper.classList.toggle('sidebar-opened');
        });
    }

    // Initialize Tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Toast Notification System
    window.showToast = function (message, type = 'info') {
        const toastContainer = document.querySelector('.flash-container') || createToastContainer();
        const toast = document.createElement('div');
        toast.className = `alert alert-${type} alert-dismissible fade show custom-alert animate-fadeInUp`;
        toast.innerHTML = `
            ${getIcon(type)} ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        toastContainer.appendChild(toast);

        // Auto-remove after 5 seconds
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(toast);
            bsAlert.close();
        }, 5000);
    };

    function createToastContainer() {
        const div = document.createElement('div');
        div.className = 'flash-container';
        div.style.cssText = 'position:fixed; top:1rem; right:1rem; z-index:9999; min-width:300px;';
        document.body.appendChild(div);
        return div;
    }

    function getIcon(type) {
        switch (type) {
            case 'success': return '<i class="bi bi-check-circle-fill me-2"></i>';
            case 'danger': return '<i class="bi bi-exclamation-circle-fill me-2"></i>';
            case 'warning': return '<i class="bi bi-exclamation-triangle-fill me-2"></i>';
            default: return '<i class="bi bi-info-circle-fill me-2"></i>';
        }
    }

    // Course Status Auto-update (Global handler)
    document.querySelectorAll('.auto-save-progress').forEach(el => {
        el.addEventListener('change', function () {
            const subjectId = this.dataset.subjectId;
            const status = this.value;
            fetch('/api/progress/update', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ subject_id: subjectId, status: status })
            })
                .then(r => r.json())
                .then(data => {
                    if (data.success) {
                        showToast('Progress updated successfully!', 'success');
                    }
                })
                .catch(err => showToast('Failed to update progress.', 'danger'));
        });
    });
});
