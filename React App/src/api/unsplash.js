import axios from "axios";

export default axios.create({
    baseURL: "https://api.unsplash.com/search/photos",
    headers: {
        Authorization: "Client-ID YIMGSq1OO41WQVX7PWROGFHmjIShPxFb-1nKxW4ouiw",
    },
});
