import React from "react";
import {
Box,
Container,
Row,
Column,
FooterLink,
Heading,
} from "./FooterStyles";

const Footer = () => {
return (
	<Box>
	<Container>
		<Row>
		<Column>
			<Heading>About</Heading>
		</Column>
		<Column>
			<Heading>App</Heading>
		</Column>
		<Column>
			<Heading>Contact</Heading>
		</Column>
		<Column>
			<Heading>Shop</Heading>
		</Column>
		</Row>
	</Container>
	</Box>
);
};
export default Footer;
