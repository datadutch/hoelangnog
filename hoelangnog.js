import { createCanvas, loadImage } from 'canvas';

export default {
  async fetch(request) {
    const canvas = createCanvas(800, 600);
    const ctx = canvas.getContext('2d');

    // Load the image
    const image = await loadImage('your_image.jpg');
    ctx.drawImage(image, 0, 0, canvas.width, canvas.height);

    // Define text and positions
    const firstLine = "Kuurne Brussel Kuurne, 2 maart 11:00";
    const currentTime = new Date();
    const eventTime = new Date(currentTime.getFullYear(), 2, 2, 11, 0);
    const timeDiff = eventTime - currentTime;
    const hoursDiff = Math.floor(timeDiff / (1000 * 60 * 60));
    const minutesDiff = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
    const secondLine = `Nog ${hoursDiff} uren en ${minutesDiff} minuten`;

    // Render text on the image
    ctx.fillStyle = 'red';
    ctx.font = '40px Arial';
    ctx.fillText(firstLine, canvas.width - ctx.measureText(firstLine).width - 50, 50);
    ctx.font = 'bold 40px Arial';
    ctx.fillText(secondLine, canvas.width - ctx.measureText(secondLine).width - 50, 110);

    // Convert canvas to a buffer and return as response
    const buffer = canvas.toBuffer('image/jpeg');
    return new Response(buffer, {
      headers: { 'Content-Type': 'image/jpeg' }
    });
  }
};
