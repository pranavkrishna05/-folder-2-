import { Request, Response } from 'express';
import { UserService } from '../../services/users/UserService';

export class UserController {
    private userService: UserService;

    constructor() {
        this.userService = new UserService();
    }

    public async register(req: Request, res: Response): Promise<Response> {
        try {
            const { email, password } = req.body;
            const user = await this.userService.register(email, password);
            return res.status(201).json({ message: 'User registered successfully', user });
        } catch (error) {
            return res.status(400).json({ message: error.message });
        }
    }
}
