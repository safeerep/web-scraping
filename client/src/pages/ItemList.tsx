import { useEffect, useState } from 'react';
import axios from 'axios';

const ItemList = () => {
    const [items, setItems] = useState<any>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<any>(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/items');
                console.log('response.data');
                console.log(response.data);
                
                setItems(response.data);
            } catch (err) {
                setError(err);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error fetching data: {error.message}</div>;

    return (
        <div>
            <h1>Scraped Items</h1>
            <ul>
                {items &&
                (
                    <li>
                        <h1>{items?.[0]?.title}</h1>
                        <p className='' style={{color: 'green'}} >{items?.[0]?.url}</p>
                        <h2>{items?.[0]?.heading}</h2>

                        <p>{items?.[0]?.first_model_name}</p>
                        <p>{items?.[0]?.description_for_first_model}</p>
                        <p>{items?.[0]?.second_model_name}</p>
                        <p>{items?.[0]?.description_for_second_model}</p>
                        <p>{items?.[0]?.third_model_name}</p>
                        <p>{items?.[0]?.description_for_third_model}</p>
                    </li>
                )}
            </ul>
        </div>
    );
};

export default ItemList;