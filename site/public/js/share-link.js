document.addEventListener('DOMContentLoaded', () => {
  const shareLink = document.getElementById('share-link');
  if (!shareLink) return;

  shareLink.addEventListener('click', async (e) => {
    e.preventDefault();
    try {
      if (navigator.share) {
        await navigator.share({
          title: document.title,
          url: window.location.href
        });
      } else {
        throw new Error('Web Share API not supported');
      }
    } catch (err) {
      try {
        await navigator.clipboard.writeText(window.location.href);
      } catch (clipErr) {
        console.error('Failed to copy link:', clipErr);
      }
    }
  });
});
