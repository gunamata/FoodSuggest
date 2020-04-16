import  React, {Component} from "react"
import {Form} from 'react-bootstrap'

class ItemList extends Component {

    constructor(props) {
        super(props)
        this.state = {
            items = [],
            label = "",
            selectedItems = []
        }
    }

    render() {
        return (
            <div>
                <Form.Group controlId="homeForm.ControlDietList">
                    <Form.Label>Select Diet(s)</Form.Label>
                    <Form.Control onChange={this.onDietSelectionChange.bind(this)} as="select" multiple>
                        {this.state.diets.map( (diet) =>
                            <option key={diet.id}>{diet.name}</option>
                        )}                                 
                    </Form.Control>
                </Form.Group>           
            </div>
        )
    }

}