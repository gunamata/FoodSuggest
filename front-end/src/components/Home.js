import React, { Component } from 'react';
import {Form, Row, Col, Table, Button} from 'react-bootstrap'
import styled from 'styled-components'

const Styles = styled.div`
    .btn-primary {
        color: #bbb;
        background-color: #222;
        border-color: #222;
    }
`;

class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
          diets: [],
          diseases: [],
          foodCategories: [],
          foodSuggestions: [],
          selectedDietItems: [],
          selectedDiseaseItems: [],
          selectedFoodCategories: []
        };
        this.getFoodSuggestion = this.getFoodSuggestion.bind(this);
    }

    componentDidMount() {
        fetch('https://crbuj19wyd.execute-api.us-east-1.amazonaws.com/dev/diet')
        .then(res => res.json())
        .then((data) => {  
          this.setState({ diets: data })
        })    
        .then(        fetch('https://crbuj19wyd.execute-api.us-east-1.amazonaws.com/dev/disease')
        .then(res => res.json())
        .then((data) => {  
          this.setState({ diseases: data })
        }))
        .then(        fetch('https://crbuj19wyd.execute-api.us-east-1.amazonaws.com/dev/food-category')
        .then(res => res.json())
        .then((data) => {  
          this.setState({ foodCategories: data })
        }))        
        .catch(console.log)        
    }

    getFoodSuggestion() {
        let s = {
                    diets: this.state.selectedDietItems,
                    diseases: this.state.selectedDiseaseItems,
                    sensitivityCategories: this.state.selectedFoodCategories
                }
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(s)
        };
        let url = 'https://crbuj19wyd.execute-api.us-east-1.amazonaws.com/dev/foodsuggest'
        fetch(url,requestOptions)
        .then(res => res.json())
        .then((data) => {  
          this.setState({ foodSuggestions: data })
        })
        .catch(console.log)         
    }

    onDietSelectionChange(e){
        let selected=[];//will be selected option in select
        let selected_opt=(e.target.selectedOptions);
        for (let i = 0; i < selected_opt.length; i++){
            selected.push(selected_opt.item(i).value)
        }
        this.setState({ selectedDietItems: selected })
    }

    onDiseaseSelectionChange(e){
        let selected=[];//will be selected option in select
        let selected_opt=(e.target.selectedOptions);
        for (let i = 0; i < selected_opt.length; i++){
            selected.push(selected_opt.item(i).value)
        }
        this.setState({ selectedDiseaseItems: selected })
    }    

    onFoodCategorySelectionChange(e){
        let selected=[];//will be selected option in select
        let selected_opt=(e.target.selectedOptions);
        for (let i = 0; i < selected_opt.length; i++){
            selected.push(selected_opt.item(i).value)
        }
        this.setState({ selectedFoodCategories: selected })
    }    

    render() {
        return (
            <div>
                <Form>
                    <Row>
                        <Col>
                            <Form.Group controlId="homeForm.ControlDietList">
                                <Form.Label>Select Diet(s)</Form.Label>
                                <Form.Control onChange={this.onDietSelectionChange.bind(this)} as="select" multiple>
                                    {this.state.diets.map( (diet) =>
                                        <option key={diet.id}>{diet.name}</option>
                                    )}                                 
                                </Form.Control>
                            </Form.Group>                
                        </Col>
                        <Col>
                            <Form.Group controlId="homeForm.ControlDiseaseList">
                                <Form.Label>Select Disease(s)</Form.Label>
                                <Form.Control onChange={this.onDiseaseSelectionChange.bind(this)} as="select" multiple>
                                    {this.state.diseases.map( (disease) =>
                                        <option key={disease.id}>{disease.name}</option>
                                    )}                                 
                                </Form.Control>
                            </Form.Group> 
                        </Col>
                        <Col>
                            <Form.Group controlId="homeForm.ControlFoodCategoriesList">
                                <Form.Label>Select Sensitivities</Form.Label>
                                <Form.Control onChange={this.onFoodCategorySelectionChange.bind(this)} as="select" multiple>
                                    {this.state.foodCategories.map( (foodcategory) =>
                                        <option key={foodcategory.id}>{foodcategory.name}</option>
                                    )}                                 
                                </Form.Control>
                            </Form.Group> 
                        </Col>                        
                    </Row>  
                    <Styles>
                        <Button variant="primary" size="lg" onClick={this.getFoodSuggestion} block>                        
                            Get Food Suggestion                        
                        </Button>
                    </Styles>
                </Form>
                <Table responsive>
                    <thead>
                        <tr>
                            <th>Food Suggestion</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.foodSuggestions.map(foodSuggestion =>
                            <tr key={foodSuggestion.id}>
                                <td>{foodSuggestion.name}</td>
                            </tr>
                        )}             
                    </tbody>
                </Table>
            </div>
        )
    }

}

export default Home