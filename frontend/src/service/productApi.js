import axios from "axios";

const URL = "http://127.0.0.1:5000/"

export const getReviews = async (product,aspect,sentiment) => {
    try {
        return await axios
            .get(`${URL}reviews/${product}/${aspect}/${sentiment}`)
            .then((response) => {
                console.log(response)
                return response;
            })
            .catch((error) => console.log(error));
    } catch (error) {
        console.log(error);
    }
};